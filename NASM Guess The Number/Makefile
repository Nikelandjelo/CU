%: %.o
	ld -m elf_i386 -s $<

%.o: %.asm
	nasm -f elf -F dwarf -g $<

