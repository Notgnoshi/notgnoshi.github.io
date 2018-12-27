texpreamble("\usepackage{amssymb}");
settings.outformat = "pdf";
size(10cm);

real xmax = 3;
real xmin = 0;
real ymax = 1.5;
real ymin = -1.5;
real step = 0.5;
real radius = 0.5;

// The domain
draw((xmin, ymin) -- (xmin, ymax), L=Label("$\mathbb R$", position=BeginPoint));
dot((xmin, (ymin + ymax) / 2));

draw((xmin + 0.3, (ymin + ymax) / 2) .. (xmin + step, (ymin + ymax) / 2 + 0.1) .. (xmin + 3*step - 0.3, (ymin + ymax) / 2), arrow=Arrow(TeXHead), L=Label("$f$", position=MidPoint, align=N));

// The range
int i = 0;
for(i = 3; i < 9; ++i)
{
    draw((xmin + i * step, ymin) -- (xmin + i * step, ymax));
    dot((xmin+i * step, (ymin + ymax) / 2));
}

label("$\cdots$", (xmin + i * step, (ymin + ymax) / 2));
label("$\mathbb R^\omega$", ((xmin + 3 * step + xmin + i * step) / 2 - 0.2, ymin-0.1));

for(i = 3; i < 8; ++i)
{
    draw((xmin + i * step, (ymin + ymax) / 2) -- (xmin + (i + 1) * step, (ymin + ymax) / 2));
}
