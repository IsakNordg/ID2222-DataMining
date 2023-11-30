clear all;
clc;

k = 4;
E = csvread('example1.dat');

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

% Assign each original point to its respective cluster
for i = 1:length(idx)
    cluster_idx = idx(i);
    clusters{cluster_idx} = [clusters{cluster_idx}; Y(i, :)];
end

% Display points in each cluster (optional)
for j = 1:k
    %fprintf('Points in Cluster %d:\n', j);
    %disp(clusters{j});
end