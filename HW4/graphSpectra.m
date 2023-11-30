clear all;
clc;

k = 2;
E = csvread('example2.dat');

% ---Step 1---
col1 = E(:,1);
col2 = E(:,2);
max_ids = max(max(col1,col2));
As= sparse(col1, col2, 1, max_ids, max_ids); 
A = full(As);

% spy(A); % Plots the adjacency matrix

% ---Step 2---
D = diag(sum(A, 2));

L = (D^(-1/2)*A*D^(-1/2));

% ---Step 3---
[vecs, vals] = eigs(L, k);

% Ortogonaliserad?
X = vecs;

% ---Step 4---
Y = normr(X);

% ---Step 5---
clusters = kmeans(Y, k);
clusters_mat = zeros(length(Y), k); % Initialize clusters_mat with the correct size

plt = plot(graph(A), 'Layout', 'force3')
cluster_colors=hsv(k);
% ---Step 6---
% Assign each original point to its respective cluster
for i = 1:k
    cluster_idx = find(clusters == i);
    clusters_mat(cluster_idx, i) = 1; 
    highlight(plt, cluster_idx , 'NodeColor', cluster_colors(i,:))
end

disp(clusters_mat);
