clear
close all

cd Data_ERA20c;

fnam = ['era20c_t2m_daymean_1900-2010_Eur_interp.nc'];  


nc_dump(fnam);
    
t2m = nc_varget(fnam, 't2m');
lon = nc_varget(fnam, 'lon');
lat = nc_varget(fnam, 'lat');

%Reading the data
quanti=0.99
for bl=1:4
    if bl==1
        n=100
    elseif bl==2
        n=50
    elseif bl==3
        n=33
    elseif bl==4
        n=25
    end
for la=1:20
    for lo=1:17
    la
        serie=double(squeeze(t2m(:,la,lo)));
        % Dopo per le anomalie       serie=diff(serie);
[theta1 theta2 CsiMax(la,lo,bl) SigmaMax(la,lo,bl) MuMax(la,lo,bl) CsiMin(la,lo,bl) SigmaMin(la,lo,bl) MuMin(la,lo,bl)]=GEV_analysis(serie,n,quanti);

        clear serie
    end
end
end
    clear t2m; save(['ERA20C_GEV.mat']);
