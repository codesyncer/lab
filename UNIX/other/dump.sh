if test ! -d "fi"
	then
		mkdir "fi"
fi
cd fi

lim=$1
ncon=1000
con="MeoworBowor"
for((i=0;i<=$ncon; ++i))
do
	echo $con > ".file"
don
euntil test $lim -lt 1
do
	cp ".file" "file"$lim
	((lim=lim-1))
done