A=imread('cameraman.tif'); %Read in image
subplot(1,2,1), imshow(A); %Display image
func=@(x) max(x(:)); %Set filter to apply
B=nlfilter(A,[3 3],func); %Apply over 3  3 neighbourhood
subplot(1,2,2), imshow(B); %Display result image B