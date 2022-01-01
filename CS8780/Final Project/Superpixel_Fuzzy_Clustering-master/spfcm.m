%Super Pixel Fuzzy C-means Algorithm in Matlab
%
%Inputs:
%******c: Number of clusters
%******X: Data Matrix consist of superpixel number,number of pixel in the
%superpixel, and features data
%******connection: Matrix jxj, showing how superpixels connected to each
%other (in this experiment I use GLCM to get the connection)
%******m: Fuzzifier as a real number
%******metric: Distance metric as a function (I use Euclidean)
%******Max: Maximum number of iterations
%******tol: Tolerance  
%******alpha: coefficient of how neighborhood superpixel affect each superpixel
%******Nfeature: number of feature data


%***********************************************
%Outputs: 
%******prediction: Predicted labels of data
%******v: Center  of clusters as a matrix c*N_features
%******save_v: saving all v for all iterations 
%******U: U Fuzzy Memberships
%***********************************************
function [prediction v U save_v] = spfcm(c, X,connection, m, metric, Max, tol,alpha,Nfeature)

[n, no] = size(X);
no=Nfeature;
%%%initialization
U = zeros([c, n]);
v = repmat(max(X(:,3:(2+Nfeature))), c, 1).*rand([c, no]);
U = rand([c, n]);
save_v=[v];
for j = 1:n
      U(:, j) = U(:, j)./sum(U(:, j));      
end  

for i  =1:c
        v(i, :)=(sum((X(:,2).*X(:,3:(2+Nfeature))+cell2mat(arrayfun(@(j){(alpha/(sum(connection(j,:))))...
        *(sum(cell2mat(arrayfun(@(a){(X(a,3:(2+Nfeature)).*X(a,2))'}, find(connection(j,:)))),2))}, [1:n]))').*...
        repmat(U(i, :)'.^m, 1, no),1))./(sum((X(:,2)+(cell2mat(arrayfun(@(j){(alpha/(sum(connection(j,:))))...
        *(sum(cell2mat(arrayfun(@(a){(X(a,2))'}, find(connection(j,:)))),2))}, [1:n]))')).*repmat(U(i, :)'.^m, 1, no),1));
end
save_v=[save_v;v];
v_old = v;
delta = 1e4;
k = 0;
while  (k<Max & delta>tol)
    for i = 1:c
      for j = 1:n
        %number of neighbor superpixels
        totaladjspx=sum(connection(j,:));
        %%%getting neighbor superpixels
        adjspxind=find(connection(j,:));    
        %%%% 1 is the index for the superpixel number 
        %%%% 2 is the number of pixel in the superpixel
        %%%% 3 is average for the first feature
        %%%% 4 is the average for the second feature and so on
        U(i, j)=1/sum(((X(j,2)*(metric(X(j,3:(2+Nfeature)),v(i,:)).^2)+((alpha/totaladjspx)*sum(X(adjspxind,2).*metric(...
        X(adjspxind,3:(2+Nfeature)),v(i,:)).^2)))./(X(j,2)*(metric(X(j,3:(2+Nfeature)),v).^2)+((alpha/totaladjspx).*...
        sum(cell2mat(arrayfun(@(a){X(a,2).*(metric(X(a,3:(2+Nfeature)),v).^2)}, adjspxind)),2)))).^(1/(m-1)));  

      end
    end
    for i = 1:c
        %%%% 1 is the index for the superpixel number 
        %%%% 2 is the number of pixel in the superpixel
        %%%% 3 is average for the first feature
        %%%% 4 is the average for the second feature and so on
        v(i, :)=(sum((X(:,2).*X(:,3:(2+Nfeature))+cell2mat(arrayfun(@(j){(alpha/(sum(connection(j,:))))...
        *(sum(cell2mat(arrayfun(@(a){(X(a,3:(2+Nfeature)).*X(a,2))'}, find(connection(j,:)))),2))}, [1:n]))').*...
        repmat(U(i, :)'.^m, 1, no),1))./(sum((X(:,2)+(cell2mat(arrayfun(@(j){(alpha/(sum(connection(j,:))))...
        *(sum(cell2mat(arrayfun(@(a){(X(a,2))'}, find(connection(j,:)))),2))}, [1:n]))')).*repmat(U(i, :)'.^m, 1, no),1));
    end
    save_v=[save_v;v];
v_new = v;
delta = max(max(abs(v_new-v_old)));
v_old = v;

k = k+1;
end
%%%%%Getting the predicted crisp labels
prediction = zeros([1, n]);
for i = 1:n
   [M, prediction(i)]=max(U(:, i));
end

end


