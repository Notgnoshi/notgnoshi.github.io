settings.outformat = "pdf";
size(10cm);

real xmax = 1;
real xmin = 0;
real ymin = 0;
real ymax = 1;

real x1 = 0.2;
real x2 = 0.6;
real radius = 0.2;

// Draw axes
draw((xmin, ymin) -- (xmax, ymin), L=Label("$X$", position=EndPoint));

// Draw U
draw(arc((x2-radius, ymin), radius, -15, 15));
draw(arc((x1+radius, ymin), radius, 165, 195));
draw((x1, ymin) -- (x2, ymin), L=Label("$U$", position=MidPoint, align=S));
