#!/bin/bash

whatsort()
{
	local where="$1"
	local size=$(du -sh "$where"*| cut -f1)
	echo $size
}
for i in *;do
	nsize=$(whatsort "$i")
	echo -e "$nsize\t$i"
done | sort -hr





