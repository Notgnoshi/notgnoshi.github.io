---
layout: post
title: Memory Mapped GPIO with the Odroid XU4
sutitle: "Read: faster GPIO than sysfs"
meta: An easy-ish to use interface for GPIO on an Odroid XU4/XU3 without using /sys/class/gpio/
---

<!-- Custom styles for the tables -->
<link rel="stylesheet" href="{{ "/assets/styles/tables.css" | prepend: site.baseurl }}">

References [here](http://odroid.com/dokuwiki/doku.php?id=en:xu3_gpio_register) and [here](http://raspberrypi.stackexchange.com/questions/600/how-does-memory-mapped-i-o-addressing-work).

<table>
	<thead>
    	<tr>
    		<th> Pin Number </th><th> GPIO name </th><th> Base Address </th><th> Offset </th><th> Name </th><th> Bit </th><th> Type </th><th> Description </th><th> Reset Value </th>
    	</tr>
	</thead>
	<tr>
		<td>15</td><td>GPX1.2</td><td rowspan="12"> 0x1340_0000 </td><td rowspan="5"> 0x0C20 </td><td> GPX1CON[2] </td><td> [11:8] </td><td rowspan="18"> RW </td><td rowspan="18"> 0x0=input, 0x1=Output, 0x2=Reserved, 0x3=Reserved, 0x4=<a href="/dokuwiki/doku.php?id=en:tracedata" class="wikilink2" title="en:tracedata" rel="nofollow">TraceData</a>, 0x5 to 0xE=Reserved, 0xF=EXT_INT</td><td rowspan="18"> 0x00 </td>
	</tr>
	<tr>
		<td>18</td><td>GPX1.3</td><td> GPX1CON[3] </td><td> [15:12] </td>
	</tr>
	 <tr>
		<td>13</td><td>GPX1.5</td><td> GPX1CON[5] </td><td> [23:20] </td>
	</tr>
	<tr>
		<td>17</td><td>GPX1.6</td><td> GPX1CON[6] </td><td> [27:24] </td>
	</tr>
	<tr>
		<td>25</td><td>GPX1.7</td><td> GPX1CON[7] </td><td> [31:28] </td>
	</tr>
	<tr>
		<td>26</td><td>GPX2.0</td><td rowspan="6"> 0x0C40 </td><td> GPX2CON[0] </td><td> [3:0] </td>
	</tr>
	<tr>
		<td>24</td><td>GPX2.1</td><td> GPX2CON[1] </td><td> [7:4] </td>
	</tr>
	<tr>
		<td>20</td><td>GPX2.4</td><td> GPX2CON[4] </td><td> [19:16] </td>
	</tr>
	<tr>
		<td>21</td><td>GPX2.5</td><td> GPX2CON[5] </td><td> [23:20] </td>
	</tr>
	<tr>
		<td>19</td><td>GPX2.6</td><td> GPX2CON[6] </td><td> [27:24] </td>
	</tr>
	<tr>
		<td>22</td><td>GPX2.7</td><td> GPX2CON[7] </td><td> [31:28] </td>
	</tr>
	<tr>
		<td>27</td><td>GPX3.1</td><td> 0x0C60 </td><td> GPX3CON[1] </td><td> [7:4] </td>
	</tr>
	<tr>
		<td>10</td><td>GPA2.4</td><td rowspan="6"> 0x1401_0000 </td><td   rowspan="4"> 0x0040 </td><td> GPA2CON[4] </td><td> [19:16] </td>
	</tr>
	<tr>
		<td>11</td><td>GPA2.5</td><td> GPA2CON[5] </td><td> [23:20] </td>
	</tr>
	<tr>
		<td>9</td><td>GPA2.6</td><td> GPA2CON[6] </td><td> [27:24] </td>
	</tr>
	<tr>
		<td>7</td><td>GPA2.7</td><td> GPA2CON[7] </td><td> [31:28] </td>
	</tr>
	<tr>
		<td>16</td><td>GPB3.2</td><td rowspan="2"> 0x00C0 </td><td> GPB3CON[2] </td><td> [11:8] </td>
	</tr>
	<tr>
		<td>14</td><td>GPB3.3</td><td> GPB3CON[3] </td><td> [15:12] </td>
	</tr>
</table>

Here's the example on the Odroid wiki webpage linked above.

```C
#include <stdio.h>
#include <fcntl.h>
#include <sys/mman.h>
#include <stdint.h>

static volatile uint32_t *gpio;

int main()
{
    int fd;

    if ((fd = open("/dev/mem", O_RDWR | O_SYNC)) < 0)
    {
        printf("Unable to open /dev/mem\n");
        return -1;
    }

    gpio = mmap(0, getpagesize(), PROT_READ | PROT_WRITE, MAP_SHARED, fd, 0x13400000);

    if (gpio < 0)
    {
        printf("mmap failed.\n");
        return -1;
    }

    // Print GPX1 configuration register.
    printf("GPX1CON register : 0x%08x\n", *(unsigned int*)(gpio + (0x0c20 >> 2)));

    // Set direction of GPX1.2 configuration register as out.
    *(gpio + (0x0c20 >> 2)) |= (0x1 << 8);
    printf("GPX1CON register : 0x%08x\n", *(unsigned int *)(gpio + (0x0c20 >> 2)));

    // GPX1.2 (pin 15) High
    *(gpio + (0x0c24 >> 2)) |= (1 << 2);
    printf("GPX1DAT register : 0x%08x\n", *(unsigned int *)(gpio + (0x0c24 >> 2)));

    // GPX1.2 (pin 15) Low
    *(gpio + (0x0c24 >> 2)) &= ~(1 << 2);
    printf("GPX1DAT register : 0x%08x\n", *(unsigned int *)(gpio + (0x0c24 >> 2)));

    return 0;
}
```
