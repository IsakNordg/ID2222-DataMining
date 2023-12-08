clear all;
clc;

k = 4;
E = csvread('example1.dat');

% ---Step 1---
% Create the adjececy matrix A
col1 = E(:,1);
col2 = E(:,2);
max_ids = max(max(col1,col2));
As= sparse(col1, col2, 1, max_ids, max_ids); 
A = full(As);

figure(1)
spy(A);
figure(2)

% ---Step 2---
% Diagonalize and create Laplacian matrix

% All neighbors of A
D = diag(sum(A, 2));

% Want high internal and low external affinity
% Diagonal elements represent every edge that leaves the cluster
% Other elements represents the ones within

L = (D^(-1/2)*A*D^(-1/2)); 

% ---Step 3---
% Calculate eigenvalues of the Laplacian matrix
[vecs, vals] = eigs(L, k);
X = vecs;   % Represent clusters as a long binary col-vector

% ---Step 4---
% Normalize the eigenvalues
Y = normr(X);

% ---Step 5---
% Cluster the original points using kmeans
clusters = kmeans(Y, k);
clusters_mat = zeros(length(Y), k); % Initialize clusters_mat with the correct size

% ---Step 6---
% Assign each original point to its respective cluster
% (and plot)
plt = plot(graph(A), 'Layout', 'force3');

colors=hsv(k);
for i = 1:k
    cluster_idx = find(clusters == i); % Finds the index of all clusters belonging to cluster i
    clusters_mat(cluster_idx, i) = 1; % Not used, but useful 
    highlight(plt, cluster_idx , 'NodeColor', colors(i,:))
end
