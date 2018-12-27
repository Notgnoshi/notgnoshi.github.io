texpreamble("\usepackage{amssymb}");
settings.outformat = "pdf";
size(10cm);

real xmax = 3;
real xmin = 0;
real ymax = 1.5;
real ymin = -1.5;
real step = 0.5;
real radius = 0.4;

int i = 0;
for(i = 0; i < 6; ++i)
{
    draw((xmin + i * step, ymin) -- (xmin + i * step, ymax));
    dot((xmin + i * step, (ymin + ymax) / 2));

    real top = 1 / (i + 1);
    real bottom = -top;

    // The first coordinate is the center of the arc, so shift it to get the arc
    // in the right spot. This keeps the curvature and arc length constant.
    draw(arc((xmin + i * step, top-radius), radius, 80, 100));
    draw(arc((xmin + i * step, bottom+radius), radius, 260, 280));
}

label("$\cdots$", (xmin + i * step, (ymin + ymax) / 2));
label("$\mathbb R^\omega$", ((xmin + i * step) / 2, ymin-0.1));
draw((xmin, (ymin + ymax) / 2) -- (xmin + (i - 1) * step, (ymin + ymax) / 2));
