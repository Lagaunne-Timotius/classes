%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%Plant and Soil vs Residue (2 Clusters)%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
image2=imread('Project1_img2.jpg');
image2_mod=double(image2);
grayscale_2=rgb2gray(image2);

%Normalized Data
grayscale_2=Normalization(double(grayscale_2));

%%%%%%%%%%%%%%Parameters
c=2;
metric=@euclidean;
Max=200;
tol=0.001;
Nfeature=1;
Compactness=10;
NumSupix=6000;
Alpha=2;
Fuzzifier=2;


%%%%%%Superpixels Extraction
Alab = rgb2lab(image2);

[L,N] = superpixels(Alab,NumSupix,'isInputLab',true,'compactness',Compactness);
%%%%%%%%Superpixels Connection
offsets = [0 1; -1 1;-1 0;-1 -1];
glcms = graycomatrix(L,'Offset',offsets,'GrayLimits',[1 N],'NumLevels',N,'Symmetric',true);
total=glcms(:,:,1)+glcms(:,:,2)+glcms(:,:,3)+glcms(:,:,4);
total_diag = diag(diag(total));
connection=(total-total_diag)>0;
%%%%%%%%%%%%Getting Superpixels  Based Feature
idx = label2idx(L);
data=[];
for labelVal = 1:N
    tempIdx = idx{labelVal};
    temp=idx(labelVal);
    [a,b]=size(temp{1});
    singledata=[labelVal,a,mean(grayscale_2(tempIdx(:)))];
    data=[data;singledata];
end    

[prediction v U save_v] = spfcm(c,data,connection,Fuzzifier,metric, Max, tol,Alpha,Nfeature);

%Visualization
figure,
subplot(1,2,1)
imagesc(image2);
subplot(1,2,2)
imagesc(grayscale_2);

final1=L;
final2=L;


for labelVal = 1:N
final1(L==labelVal)=U(1,labelVal);
final2(L==labelVal)=U(2,labelVal);
end    
figure,
subplot(1,2,1)
imagesc(final1,[0,1]);colormap jet
title(sprintf('Cluster 1'))
axis off

subplot(1,2,2)
imagesc(final2,[0,1]);colormap jet
title(sprintf('Cluster 2'))
axis off

U_save=U;

%%%Plant vs Soil and Residue (2 Clusters)%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
image2=imread('Project1_img2.jpg');
image2_mod=double(image2);
exG_2=2*image2_mod(:,:,2)-image2_mod(:,:,1)-image2_mod(:,:,3);

%Normalized Data
exG_2=Normalization(double(exG_2));


%%%%%%%%%%%%%%Parameters
c=2;
metric=@euclidean;
Max=200;
tol=0.001;
Nfeature=1;
Compactness=10;
NumSupix=5000;
Alpha=0.5;
Fuzzifier=2;


%%%%%%Superpixels Extraction
Alab = rgb2lab(image2);

[L,N] = superpixels(Alab,NumSupix,'isInputLab',true,'compactness',Compactness);
%%%%%%%%Superpixels Connection
offsets = [0 1; -1 1;-1 0;-1 -1];
glcms = graycomatrix(L,'Offset',offsets,'GrayLimits',[1 N],'NumLevels',N,'Symmetric',true);
total=glcms(:,:,1)+glcms(:,:,2)+glcms(:,:,3)+glcms(:,:,4);
total_diag = diag(diag(total));
connection=(total-total_diag)>0;
%%%%%%%%%%%%Getting Superpixels  Based Feature
idx = label2idx(L);
data=[];
for labelVal = 1:N
    tempIdx = idx{labelVal};
    temp=idx(labelVal);
    [a,b]=size(temp{1});
    singledata=[labelVal,a,mean(exG_2(tempIdx(:)))];
    data=[data;singledata];
end    

[prediction v U ] = spfcm(c,data,connection,Fuzzifier,metric, Max, tol,Alpha,Nfeature);

%Visualization
figure,
subplot(1,2,1)
imagesc(image2);
title('Original Image')
axis off
subplot(1,2,2)
imagesc(exG_2);
title('exG')
axis off

final1=L;
final2=L;

for labelVal = 1:N
final1(L==labelVal)=U(1,labelVal);
final2(L==labelVal)=U(2,labelVal);
end    
figure,
subplot(1,2,1)
imagesc(final1,[0,1]);colormap jet
title(sprintf('Cluster 1'))
axis off

subplot(1,2,2)
imagesc(final2,[0,1]);colormap jet
title(sprintf('Cluster 2'))
axis off

%%%%%%%%%%%%%%%%%%%%%%%%%%Manually substracting the plant from soil and plant membership %%%%%%%%%%%%%%%%%%%%%%%%% 
% final1=L;
% final2=L;
% final3=L;
% residue=U_save(1,:);
% plant=U(1,:);
% soil=U_save(2,:)-U(1,:);
% soil(soil<0)=0;
% 
% final1=L;
% final2=L;
% final3=L;
% 
% 
% for labelVal = 1:N
% final1(L==labelVal)=plant(1,labelVal);
% final2(L==labelVal)=soil(1,labelVal);
% final3(L==labelVal)=residue(1,labelVal);
% end    
% figure,
% subplot(1,3,1)
% imagesc(final1,[0,1]);colormap jet
% title(sprintf('Cluster 1'))
% axis off
% 
% subplot(1,3,2)
% imagesc(final2,[0,1]);colormap jet
% title(sprintf('Cluster 2'))
% axis off
% 
% subplot(1,3,3)
% imagesc(final3,[0,1]);colormap jet
% title(sprintf('Cluster 3'))
% axis off
% 
% figure,scatter(exG_2(:),grayscale_2(:));
% hold on
% scatter(v(:,2),v(:,1),'red')
% xlabel('exG')
% ylabel('grayscale')


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%Plant vs Soil and Residue (3 Clusters)
%%%Inputted altogether
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
image2=imread('Project1_img2.jpg');
image2_mod=double(image2);
exG_2=2*image2_mod(:,:,2)-image2_mod(:,:,1)-image2_mod(:,:,3);
grayscale_2=rgb2gray(image2);
%Normalized Data
exG_2=Normalization(exG_2);
grayscale_2=Normalization(double(grayscale_2));
%%%%%%%%%%%%%%Parameters
c=3;
metric=@euclidean;
Max=200;
tol=0.001;
Nfeature=2;
Compactness=10;
NumSupix=5000;
Alpha=2;
Fuzzifier=2;


%%%%%%Superpixels Extraction
Alab = rgb2lab(image2);

[L,N] = superpixels(Alab,NumSupix,'isInputLab',true,'compactness',Compactness);
%%%%%%%%Superpixels Connection
offsets = [0 1; -1 1;-1 0;-1 -1];
glcms = graycomatrix(L,'Offset',offsets,'GrayLimits',[1 N],'NumLevels',N,'Symmetric',true);
total=glcms(:,:,1)+glcms(:,:,2)+glcms(:,:,3)+glcms(:,:,4);
total_diag = diag(diag(total));
connection=(total-total_diag)>0;
%%%%%%%%%%%%Getting Superpixels  Based Feature
idx = label2idx(L);
data=[];
for labelVal = 1:N
    tempIdx = idx{labelVal};
    temp=idx(labelVal);
    [a,b]=size(temp{1});
    singledata=[labelVal,a,mean(exG_2(tempIdx(:))),mean(grayscale_2(tempIdx(:)))];
    data=[data;singledata];
end    

[prediction v U save_v] = spfcm(c,data,connection,Fuzzifier,metric, Max, tol,Alpha,Nfeature);

%Visualization
figure,
subplot(1,3,1)
imagesc(image2);
subplot(1,3,2)
imagesc(exG_2);
subplot(1,3,3)
imagesc(grayscale_2);
final1=L;
final2=L;
final3=L;

for labelVal = 1:N
final1(L==labelVal)=U(1,labelVal);
final2(L==labelVal)=U(2,labelVal);
final3(L==labelVal)=U(3,labelVal);
end    
figure,
subplot(1,3,1)
imagesc(final1,[0,1]);colormap jet
title(sprintf('Cluster 1'))
axis off

subplot(1,3,2)
imagesc(final2,[0,1]);colormap jet
title(sprintf('Cluster 2'))
axis off

subplot(1,3,3)
imagesc(final3,[0,1]);colormap jet
title(sprintf('Cluster 3'))
axis off


