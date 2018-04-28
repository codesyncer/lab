.model small
.data
	msg db 'Hello World$'
.code
adder:
	mov ax, @data
	mov ds, ax
	mov dx, offset msg
	mov ah, 9h
	int 21h
	mov ah, 4ch
	int 21h
end adder
