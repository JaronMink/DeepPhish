
for f in *.png; do
  convert ./"$f" ./"${f%.png}.pdf"
done
