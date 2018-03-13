A=imread('cameraman.tif'); %Read in an image
[rows dims]=size(A); %Get image dimensions
Abuild=zeros(size(A)); %Construct zero image of equal size
%Randomly sample 1% of points only and convolve with Gaussian PSF
sub=rand(rows.*dims,1)<0.01;
Abuild(sub)=A(sub); h=fspecial('gaussian',[10 10],2);
B10=filter2(h,Abuild);
subplot(1,2,1), imagesc(Abuild); axis image; axis off;colormap(gray); title('Object points')
subplot(1,2,2), imagesc(B10); axis image; axis off;colormap(gray); title('Response of LSI system')