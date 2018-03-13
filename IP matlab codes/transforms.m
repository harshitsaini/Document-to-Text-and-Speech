%------LOGARITHIC--------%
I=imread('cameraman.tif'); %Read in image
subplot(2,2,1), imshow(I); %Display image
Id=im2double(I);
Output1=2*log(1+Id);
Output2=3*log(1+Id);
Output3=5*log(1+Id);
subplot(2,2,2), imshow(Output1); %Display result images
subplot(2,2,3), imshow(Output2);
subplot(2,2,4), imshow(Output3);


%------EXPONENTIAL--------%
I=imread('cameraman.tif'); %Read in image
subplot(2,2,1), imshow(I); %Display image
Id=im2double(I);
Output1=4*(((1+0.3).^(Id))-1);
Output2=4*(((1+0.4).^(Id))-1);
Output3=4*(((1+0.6).^(Id))-1);
subplot(2,2,2), imshow(Output1); %Display result images
subplot(2,2,3), imshow(Output2);
subplot(2,2,4), imshow(Output3);

%-------POWER-LAW---------%
I=imread('cameraman.tif'); %Read in image
subplot(2,2,1), imshow(I); %Display image
Id=im2double(I);
Output1=2*(Id.^0.5);
Output2=2*(Id.^1.5);
Output3=2*(Id.^3.0);
subplot(2,2,2), imshow(Output1); %Display result images
subplot(2,2,3), imshow(Output2);
subplot(2,2,4), imshow(Output3);

%-------GAMMA-CORRECTION----%
A=imread('cameraman.tif'); %Read in image
subplot(1,2,1), imshow(A); %Display image
B=imadjust(A,[0 1],[0 1],1./3); %Map input grey values of image A in range 0 1 to
%an output range of 0 1 with gamma factor of 1/3
%(i.e. r¼3).
%Type  doc imadjust for details of possible syntaxes
subplot(1,2,2), imshow(B); %Display result.