function Norm_Data=Normalization(Data)

Norm_Data=(Data-min(Data(:)))/(max(Data(:))-min(Data(:)));

end