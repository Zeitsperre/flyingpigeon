function  [theta1 theta2 CsiMax SigmaMax MuMax CsiMin SigmaMin MuMin]=GEV_analysis(variab,n,quanti)



if quanti < 0.5
    warning('Quantile too small to obtain reliable estimates on theta')
end


if length(variab) < 10000
    warning('Series too short to perform a reliable analysis')
end


    [theta1]=extremal_Sueveges(variab,quanti);
    [theta2]=extremal_FerroSegers(variab,quanti);
    s=length(variab);
    m=fix(s/n)-2; 
    init=1;
for i=1:n-init
    
    % For  extracting the maxima
    
    dmax(i)=max(variab(((i+init-1)*m+1):(i+init)*m));
    dmin(i)=min(variab(((i+init-1)*m+1):(i+init)*m));

     
end

    
%Maxima    
    [tpar tpari]=gevfit(dmax);
     CsiMax=tpar(1);
     SigmaMax=tpar(2);
     MuMax=tpar(3);
     
     [tpar tpari]=gevfit(dmin);
     CsiMin=tpar(1);
     SigmaMin=tpar(2);
     MuMin=tpar(3);   
     
    


end