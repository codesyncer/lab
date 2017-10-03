.model small
.stack
.data
	len dw 22
	scr db "INFORMATION TECHNOLOGY$"
	dst db "Hello$"
	pls db "save me!!!$"
.code
start:
	mov ax, @data
	mov ds, ax

	mov dx, offset dst
	mov ah, 9h
	int 21h

	mov dl, 10
	mov ah, 2h
	int 21h

	mov si, 0
	mov cx, len
	A:
		mov al, scr[si]
		mov dst[si], al
		inc si
		loop A
	mov dst[si], '$'

	mov dx, offset dst
	mov ah, 9h
	int 21h

	mov ah, 4ch
	int 21h
end start
