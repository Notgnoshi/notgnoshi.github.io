settings.outformat = "pdf";
size(10cm);

real xmax = 1;
real xmin = 0;
real ymax = 1;
real ymin = 0;
real step = 0.2;

int i = 0;
for(i = 0; i < 4; ++i)
{
    draw((xmin + i * step, ymin) -- (xmin + i * step, ymax), L=Label("$X_" + string(i) + "$", position=BeginPoint));
}

label("$\cdots$", (xmin + i * step, (ymin + ymax) / 2));
