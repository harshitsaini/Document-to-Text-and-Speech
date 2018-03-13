A=imread('peppers.png'); %Read in test card image
A=rgb2gray(A);
FA=fft2(A); FA=fftshift(FA); %Take FFT and centre it
PSF=fspecial('gaussian',size(A),6); %Define PSF
%B = imgaussfilt3(A,sigma)
%PSF = imgaussfilt3(gpuArray(A),6);
OTF=fft2(PSF); OTF=fftshift(OTF); %Calculate corresponding OTF
Afilt=ifft2(OTF.*FA);
Afilt=fftshift(Afilt);
%Calculate filtered image
subplot(1,4,1);imshow(A,[]);
colormap(gray);
%Display results
subplot(1,4,2); imagesc(log(1+(PSF)));
axis image; axis off;
subplot(1,4,3); imagesc(log(1+abs(OTF))); axis image; axis off;
subplot(1,4,4); imagesc(abs(Afilt)); axis
image; axis off;
PSF=fspecial('gaussian',size(A),6); %Define PSF
OTF=fft2(PSF); OTF=fftshift(OTF); %Calculate corresponding OTF
rlow=(size(A,1)./2)+3; rhigh=(size(A,1)./2)+3;
%Define range to be altered
clow=(size(A,2)./2)+3; chigh=(size(A,2)./2)+3;
Fphase=angle(OTF); %Extract Fourier phase
Fphase(rlow:rhigh,clow:chigh)= Fphase(rlow:rhigh,clow:chigh)+0.*pi.*rand;
%Add random component to selected phase
OTF=abs(OTF).*exp(i.*Fphase); %Recombine phase and modulus
Afilt=ifft2(OTF.*FA);
Afilt=fftshift(Afilt);
%Calculate filtered image
psfnew=abs(fftshift((otf2psf(OTF)))); %Calculate corresponding PSF
subplot(1,4,2); imagesc(log(1+psfnew));
axis image; axis off; colormap(gray);
subplot(1,4,3); imagesc(log(1+abs(OTF))); axis image; axis off;
subplot(1,4,4); imagesc(abs(Afilt));
axis image; axis off;
PSF=fspecial('motion',30,30); %Define motion PSF
OTF=psf2otf(PSF,size(A));
OTF=fftshift(OTF);
%Calculate corresponding OTF
Afilt=ifft2(OTF.*FA); %Calculate filtered image
subplot(1,4,1);imshow(A,[]); %Display results
subplot(1,4,2); imshow(log(1+PSF),[]);
subplot(1,4,3); imshow(log(1+abs(OTF)),[])
subplot(1,4,4); imshow(abs(Afilt),[]);