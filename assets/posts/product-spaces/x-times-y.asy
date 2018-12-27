settings.outformat = "pdf";
size(10cm);

real xmax = 1;
real xmin = 0;
real ymax = 1;
real ymin = 0;

real x1 = 0.2;
real x2 = 0.6;
real y1 = 0.4;
real y2 = 0.7;
real radius = 0.2;

// Draw axes
draw((xmin, ymin) -- (xmax, ymin), L=Label("$X$", position=EndPoint));
draw((xmin, ymin) -- (xmin, ymax), L=Label("$Y$", position=EndPoint));

// Draw the inverse projection of the open sets onto the product space
filldraw((x1, ymin) -- (x1, ymax) -- (x2, ymax) -- (x2, ymin) -- cycle, palegray, dashed);
label("$\pi_1^{-1}(U)$", (x1 + (x2 - x1) / 2, ymax-0.05));

filldraw((xmin, y1) -- (xmax, y1) -- (xmax, y2) -- (xmin, y2) -- cycle, palegray, dashed);
label("$\pi_2^{-1}(V)$", (xmax-0.12, y1 + (y2 - y1) / 2));

// Draw the intersection
filldraw((x1, y1) -- (x2, y1) -- (x2, y2) -- (x1, y2) -- cycle, mediumgray, dashed);
label("$U \times V$", (x1 + (x2 - x1) / 2, y1 + (y2 - y1) / 2));

// Draw U and V
draw(arc((x2-radius, ymin), radius, -15, 15));
draw(arc((x1+radius, ymin), radius, 165, 195));
draw((x1, ymin) -- (x2, ymin), L=Label("$U$", position=MidPoint, align=S));

draw(arc((xmin, y1+radius), radius, 255, 285));
draw(arc((xmin, y2-radius), radius, 75, 105));
draw((xmin, y1) -- (xmin, y2), L=Label("$V$", position=MidPoint, align=W));
