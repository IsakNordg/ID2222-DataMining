clear all;
clc;

k = 5;

E = csvread('example1.dat');

col1 = E(:,1);
col2 = E(:,2);
max_ids = max(max(col1,col2));
As= sparse(col1, col2, 1, max_ids, max_ids); 
A = full(As);

% spy(A); % Plots the adjacency matrix

D = diag(sum(A, 2));

D_inv_sqrt = diag(1./sqrt(diag(D)));
L = D_inv_sqrt * A * D_inv_sqrt;

[vecs, vals] = eigs(L, k, 'largestabs');
[V D] = eigs(L, k, 'SA');

% Ortogonaliserad?
X = vecs;

Y = normr(X);

% Apply K-means clustering
[idx, centers] = kmeans(Y, k);

clusters = cell(1, k);

% Assign each original point to its respective cluster
for i = 1:length(idx)
    cluster_idx = idx(i);
    clusters{cluster_idx} = [clusters{cluster_idx}; Y(i, :)];
end

% Display points in each cluster (optional)
for j = 1:k
    fprintf('Points in Cluster %d:\n', j);
    disp(clusters{j});
end