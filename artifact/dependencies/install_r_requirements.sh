#!/usr/bin/bash

DIR="$(cd "$(dirname "$0")" && pwd)"

sudo Rscript -e "install.packages('devtools', repos='http://cran.us.r-project.org')"
sudo Rscript -e "install.packages('https://cran.r-project.org/src/contrib/Archive/nloptr/nloptr_1.2.1.tar.gz', repos=NULL, type='source')"
while IFS=" " read -r package version; 
do 
  sudo Rscript -e "devtools::install_version('"$package"', version='"$version"', repos ='http://cran.us.r-project.org')"; 
done < "$DIR/r-requirements.txt"
