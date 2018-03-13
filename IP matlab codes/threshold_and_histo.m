%------------OTSU THESHOLDING-----------%
I=imread('coins.png'); %Read in image
level=graythresh(I); %Get OTSU threshold
It=im2bw(I, level); %Threshold image
imshow(It); %Display it

%-----------ADAPTIVE THRESHOLDING-------%
I=imread('rice.png'); %Read in image
Im=imfilter(I,fspecial('average',[1 1]),'replicate'); %Create mean image
It=I+(Im-20); %Subtract mean image(þ constant C¼20)
Ibw=im2bw(It,0.0); %Threshold result at 0 (keep þve results only)
subplot(1,2,1), imshow(I); %Display image
subplot(1,2,2), imshow(It); %Display result


%----------CONTRAST STRETCHING---------%
I=imread('pout.tif'); %Read in image
Ics=imadjust(I,stretchlim(I, [0.05 0.95]),[]); %Stretch contrast using method 1
subplot(2,2,1), imshow(I); %Display image
subplot(2,2,2), imshow(Ics); %Display result

subplot(2,2,3), imhist(I); %Display input histogram
subplot(2,2,4), imhist(Ics); %Display output histogram

%----------HISTOGRAM EQUALIZATION--------%
I=imread('pout.tif'); %Read in image
Ieq=histeq(I);
subplot(2,2,1), imshow(I); %Display image
subplot(2,2,2), imshow(Ieq); %Display result
subplot(2,2,3), imhist(I); %Display histogram of image
subplot(2,2,4), imhist(Ieq); %Display histogram of result

%-----------HISTOGRAM MATCHING-----------%
I=imread('pout.tif');
pz=0:255; %Define ramp like pdf as desired output histogram
Im=histeq(I, pz); %Supply desired histogram to perform matching
subplot(2,3,1), imshow(I); %Display image
subplot(2,3,2), imshow(Im); %Display result
subplot(2,3,3), plot(pz); %Display distribution t
subplot(2,3,4), imhist(I); %Display histogram of image
subplot(2,3,5), imhist(Im); %Display histogram of result

%----ADAPTIVE HISTOGRAM EQUALIZATION-----%
I=imread('pout.tif'); %Read in image
I1=adapthisteq(I,'clipLimit',0.02,'Distribution','rayleigh');
I2=adapthisteq(I,'clipLimit',0.02,'Distribution','exponential');
I3=adapthisteq(I,'clipLimit',0.08,'Distribution','uniform');
subplot(2,2,1), imshow(I); subplot(2,2,2), imshow(I2); %Display orig. þ output
subplot(2,2,3), imshow(I2); subplot(2,2,4), imshow(I3); %Display outputs

%--HISTOGRAM OPERATIONS ON COLOUR IMAGES--%
I=imread('autumn.tif'); %Read in image
Ihsv=rgb2hsv(I); %Convert original to HSV image, I2
V=histeq(Ihsv(:,:,3)); %Histogram equalise V (3rd) channel of I2
Ihsv(:,:,3)=V; %Copy equalized V plane into (3rd) channel I2
Iout=hsv2rgb(Ihsv); %Convert I2 back to RGB form
subplot(1,2,1), imshow(I);
subplot(1,2,2), imshow(Iout);