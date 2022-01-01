clear all
close all
clc

%%%Plant vs Not Plant (2 Clusters)%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
image1=imread('Project1_img1.jpg');
image1_mod=double(image1);
exG_1=2*image1_mod(:,:,2)-image1_mod(:,:,1)-image1_mod(:,:,3);
%Normalized Data
exG_1=Normalization(exG_1);
%Visualization
figure,
subplot(1,2,1)
imagesc(image1);
title('Original Image')
axis off
subplot(1,2,2)
imagesc(exG_1);
title('exG')
axis off

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%Number of superpixels 500,1000,3000,6000
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%Fix
%%Clusters=2 (Using Project1_img1.jpg)
%%Fuzzifier=2
%%Compactness=10
%%Alpha=0.3

%%%%%%%%%%%%%%Parameters
c=2;
m=2;
metric=@euclidean;
Max=100;
alpha=0.3;
tol=0.001;
Nfeature=1;
Compactness=10;
NumSupix=[500,1000,3000,6000];
figure,

%%%%%%Superpixels Extraction
Alab = rgb2lab(image1);

for i=1:length(NumSupix)
[L,N] = superpixels(Alab,NumSupix(i),'isInputLab',true,'compactness',Compactness);
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
    singledata=[labelVal,a,mean(exG_1(tempIdx(:)))];
    data=[data;singledata];
end    

[prediction v U] = spfcm(c,data,connection,m,metric, Max, tol,alpha,Nfeature);

%%%%making sure we have the same cluster 
%Output
final=L;
cmap=2;
if v(1)>v(2)
    cmap=1;
end

for labelVal = 1:N
final(L==labelVal)=U(cmap,labelVal);
end    
subplot(2,2,i)
imagesc(final,[0,1]);colormap jet
title(sprintf('Number of Superpixels: %s',num2str(NumSupix(i))))
axis off

end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%Compactness of superpixels 3,10,15,20
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%Parameters
c=2;
m=2;
metric=@euclidean;
Max=100;
alpha=0.3;
tol=0.001;
Nfeature=1;
Compactness=[1,5,10,20];
NumSupix=3000;
figure,

%%%%%%Superpixels Extraction
Alab = rgb2lab(image1);

for i=1:length(Compactness)
[L,N] = superpixels(Alab,NumSupix,'isInputLab',true,'compactness',Compactness(i));
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
    singledata=[labelVal,a,mean(exG_1(tempIdx(:)))];
    data=[data;singledata];
end    

[prediction v U] = spfcm(c,data,connection,m,metric, Max, tol,alpha,Nfeature);

%%%%making sure we have the same cluster 
%Output
final=L;
cmap=2;
if v(1)>v(2)
    cmap=1;
end

for labelVal = 1:N
final(L==labelVal)=U(cmap,labelVal);
end    
subplot(2,2,i)
imagesc(final,[0,1]);colormap jet
title(sprintf('Compactness: %s',num2str(Compactness(i))))
axis off

end

%%%%%Alpha1 0,0.1,0.3,0.5,0.7,1

%%%%%Alpha2 1,2,4,8


%%%%%%%%%%%%%%Parameters
c=2;
m=2;
metric=@euclidean;
Max=100;
alpha=0.3;
tol=0.001;
Nfeature=1;
Compactness=10;
NumSupix=3000;
Alpha=[1,2,4,8];
figure,

%%%%%%Superpixels Extraction
Alab = rgb2lab(image1);

for i=1:length(Alpha)
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
    singledata=[labelVal,a,mean(exG_1(tempIdx(:)))];
    data=[data;singledata];
end    

[prediction v U] = spfcm(c,data,connection,m,metric, Max, tol,Alpha(i),Nfeature);

%%%%making sure we have the same cluster 
%Output
final=L;
cmap=2;
if v(1)>v(2)
    cmap=1;
end

for labelVal = 1:N
final(L==labelVal)=U(cmap,labelVal);
end    
subplot(2,2,i)
imagesc(final,[0,1]);colormap jet
title(sprintf('Alpha: %s',num2str(Alpha(i))))
axis off

end




%%%%%Fuzzifier 2,4,8


%%%%%%%%%%%%%%Parameters
c=2;
m=2;
metric=@euclidean;
Max=100;
alpha=0.3;
tol=0.001;
Nfeature=1;
Compactness=10;
NumSupix=3000;
Alpha=0.3;
Fuzzifier=[2,4,8];
figure,

%%%%%%Superpixels Extraction
Alab = rgb2lab(image1);

for i=1:length(Fuzzifier)
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
    singledata=[labelVal,a,mean(exG_1(tempIdx(:)))];
    data=[data;singledata];
end    

[prediction v U] = spfcm(c,data,connection,Fuzzifier(i),metric, Max, tol,Alpha,Nfeature);

%%%%making sure we have the same cluster 
%Output
final=L;
cmap=2;
if v(1)>v(2)
    cmap=1;
end

for labelVal = 1:N
final(L==labelVal)=U(cmap,labelVal);
end    
subplot(1,3,i)
imagesc(final,[0,1]);colormap jet
title(sprintf('Fuzzifier: %s',num2str(Fuzzifier(i))))
axis off

end

