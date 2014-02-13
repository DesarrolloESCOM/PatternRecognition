warning off all
imagenOriginal = imread('peppers.png');
imagenRoja = imagenOriginal;
imagenAzul = imagenOriginal;
imagenVerde = imagenOriginal;
%% cambiando la imagen orignal a roja
imagenRoja(:,:,2)=0;
imagenroja(:,:,3)=0;
%% cambiando la imagen original a verde
imagenVerde(:,:,1) = 0;
imagenVerde(:,:,3) = 0;
%% cambiando la imagen original a azul
imagenAzul(:,:,1) = 0;
imagenAzul(:,:,2) = 0;
%% se muestran las imagenes 
%imshow(imagenRoja)
%imshow(imagenVerde)
%imshow(imagenAzul)
%% se guardan en una imagen final
matrizFinalDeImagenes = [imagenOriginal imagenRoja; imagenVerde imagenAzul];
matrizFinalDeImagenes2 = [imagenOriginal; imagenRoja; imagenVerde; imagenAzul];
% tresColoresHorizontal
tresColores = imagenOriginal;
% tresColoresVertical
tresColoresVertical = imagenOriginal;
% cruz extraña
imagenCruz = imagenOriginal;
%whos
tamano = 512/3;
tamano2 = 384/3;
%% se activa el rojo
tresColores(:,(1:tamano),2) = 0;
tresColores(:,(1:tamano),3) = 0;
%% se activa el verde
tresColores(:,((tamano+1):(2*tamano)),1) = 0;
tresColores(:,((tamano+1):(2*tamano)),3) = 0;
%% se activa el azul
tresColores(:,(((tamano*2+1):(tamano*3))),1)=0;
tresColores(:,(((tamano*2+1):(tamano*3))),2)=0;
%imshow(matrizFinalDeImagenes2)
%imshow(tresColores)
%% Se activan los colores en la imagen vertical  %%
% se activa el rojo
tresColoresVertical((1:tamano2),:,2)=0;
tresColoresVertical((1:tamano2),:,3)=0;
%se activa el verde
tresColoresVertical((tamano2+1:tamano2*2),:,1)=0;
tresColoresVertical((tamano2+1:tamano2*2),:,3)=0;
%se activa el rojo
tresColoresVertical((tamano2*2+1:tamano2*3),:,1)=0;
tresColoresVertical((tamano2*2+1:tamano2*3),:,2)=0;
%imshow(tresColoresVertical);
%% Se activan los valores de la imagen para que aparezcan los filtros en cruz %%
%imagenCruz(:,:,1) = 0;
%imagenCruz(:,:,3) = 0;
% se ponen los cuadrados rojos en la parte superior
% primer cuadro rojo
imagenCruz((1:100),(1:100),3)=0;
imagenCruz((1:100),(1:100),2)=0;
% parte verde
imagenCruz((1:100),(101:412),1)=0;
imagenCruz((1:100),(101:412),3)=0;
% segundo cuadro en rojo
imagenCruz((1:100),(413:end),3)=0;
imagenCruz((1:100),(413:end),2)=0;
% parte mas grande verde
imagenCruz((101:284),:,1)=0;
imagenCruz((101:284),:,3)=0;
% primer cuadro azul
imagenCruz((285:end),(1:100),1)=0;
imagenCruz((285:end),(1:100),2)=0;
% parte verde
imagenCruz((285:end),(101:412),1)=0;
imagenCruz((285:end),(101:412),3)=0;
% segundo cuadro en rojo
imagenCruz((285:end),(413:end),1)=0;
imagenCruz((285:end),(413:end),1)=0;
% find()



imshow(imagenCruz);

