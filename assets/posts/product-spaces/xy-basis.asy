settings.outformat = "pdf";
size(10cm);

real xmax = 1;
real xmin = 0;
real ymax = 1;
real ymin = 0;
real step = 0.3;
real radius = 0.2;

real x1 = 0.2;
real x2 = 0.5;
real y1 = 0.4;
real y2 = 0.8;

draw((xmin, ymin) -- (xmin, ymax), L=Label("$X$", position=BeginPoint));
draw((xmin+step, ymin) -- (xmin+step, ymax), L=Label("$Y$", position=BeginPoint));

filldraw((xmin, x1) -- (xmin, x2) -- (xmin+step, y2) -- (xmin+step, y1) -- cycle, palegray, dashed);
label("$U \times V$", (xmin+step/2, ((x1 + x2) / 2 + (y1 + y2) / 2) / 2));

draw(arc((xmin, x1+radius), radius, 255, 285));
draw(arc((xmin, x2-radius), radius, 75, 105));
draw((xmin, x1) -- (xmin, x2), L=Label("$U$", position=MidPoint, align=W));

draw(arc((xmin+step, y1+radius), radius, 255, 285));
draw(arc((xmin+step, y2-radius), radius, 75, 105));
draw((xmin+step, y1) -- (xmin+step, y2), L=Label("$V$", position=MidPoint, align=E));
