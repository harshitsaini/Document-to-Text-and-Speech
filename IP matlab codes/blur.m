I = imread('cameraman.tif');
imshow(I);
H = fspecial('motion',20,45);
MotionBlur = imfilter(I,H,'replicate');
imshow(MotionBlur);
H = fspecial('disk',10);
blurred = imfilter(I,H,'replicate'); 
imshow(blurred);
