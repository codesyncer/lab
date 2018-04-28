.model small
.stack
.data
	str db "INFORMATION TECHNOLOGY$"
	rev db ?
	len dw 22
.code
start:
	mov ax, @data
	mov ds, ax

	mov si, len
	mov di, 0
	sub si, 1
	mov cx, len
	A:
		mov al, str[si]
		mov rev[di], al
		inc di
		dec si
		loop A
	mov rev[di], '$'

	mov dx, offset rev
	mov ah, 9h
	int 21h

	mov ah, 4ch
	int 21h
end start