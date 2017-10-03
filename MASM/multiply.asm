.model small
.stack
.data
	a db 2
	b db 3
	pro db ?
.code
start:
	mov ax, @data
	mov ds, ax

	mov al, a
	mul b
	mov pro, al

	mov dl, pro
	add dl, '0'
	mov ah, 2h
	int 21h

	mov ah, 4ch
	int 21h
end start
