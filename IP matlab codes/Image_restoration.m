A=rgb2gray(imread('peppers.png')); B=fft2(A); B=fftshift(B); %Read in image and take FT
[x y]=size(A); [X Y]=meshgrid(1:x,1:y); %Construct Gaussian PSF
h=exp( (X-x/2).^2./48).*exp( (Y-y/2).^2./48); %extending over entire array
H=psf2otf(h,size(h)); H=fftshift(H); %Get OTF corresponding to PSF
g=ifft2(B.*H); g=abs(g); %Generate blurred image via
%Fourier domain
G=fft2(g); G=fftshift(G); %Take FT of image
indices=find(H>1e-6); %Do inverse filtering AVOIDING
F=zeros(size(G)); F(indices)=G(indices)./H(indices);
%small values in OTF !!
f=ifft2(F); f=abs(f); %Inverse FT to get filtered image
subplot(1,4,1), imshow(g,[min(min(g))
max(max(g))]);
%Display ?original? blurred image
subplot(1,4,2), imagesc(h); axis square; axis off; %Display PSF
subplot(1,4,3), imagesc(abs(H)); axis square; axis off; %Display MTF
subplot(1,4,4), imagesc(f); axis square; axis tight;
axis off;



% Weiner Westrom Filter
I = rgb2gray(imread('peppers.png'));I=double(I); %Read in image
noise =15.*randn(size(I)); %Generate noise
PSF = fspecial('motion',21,11); %Generate motion PSF
Blurred = imfilter(I,PSF,'circular'); %Blur image
BlurredNoisy ¼ Blurred þ noise; %Add noise to blurred image
NSR = sum(noise(:).^2)/sum(I(:).^2); % Calculate SCALAR noise to power ratio
NP = abs(fftn(noise)).^2; %Calculate noise power spectrum
NPOW = sum(NP(:))/prod(size(noise)); %Calculate average power in noise spectrum
NCORR = fftshift(real(ifftn(NP))); %Get autocorrelation function of the noise,
%centred using fftshift
IP = abs(fftn(I)).^2; %Calculate image power spectrum
IPOW = sum(IP(:))/prod(size(I)); %Calculate average power in image spectrum
ICORR = fftshift(real(ifftn(IP))); %Get autocorrelation function of the image,
%centred using fftshift
NSR = NPOW./IPOW; %SCALAR noise to signal power ratio
subplot(131);imshow(BlurredNoisy,[min(min(BlurredNoisy)) max(max(BlurredNoisy))]);
%Display blurred and noisy image';
subplot(132);imshow(deconvwnr(BlurredNoisy,PSF,NSR),[]);
%Wiener filtered PSF and scalar noise/
%signal power ratio
subplot(133);imshow(deconvwnr(BlurredNoisy,PSF,NCORR,ICORR),[]);
%Wiener filtered PSF and noise and signal
%autocorrelations