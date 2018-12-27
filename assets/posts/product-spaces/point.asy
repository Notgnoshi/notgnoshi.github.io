settings.outformat = "pdf";
size(10cm);

void pathlabel(picture pic=currentpicture, Label L, path g,
               real position=0.5, align align=NoAlign, bool sloped=false,
               pen p=currentpen, filltype filltype=NoFill) {
    Label L2 = Label(L, align, p, filltype, position=Relative(position));
    if (sloped) {
        pair direction = dir(g, reltime(g, position));
        real angle = degrees(atan2(direction.y, direction.x));
        L2 = rotate(angle)*L2;
    }
    label(pic, L2, g);
}

real xmax = 1;
real xmin = 0;
real ymax = 1;
real ymin = 0;
real step = 0.3;

real x1 = 0.8;
real y1 = 0.5;
real x2 = 0.1;
real y2 = 0.65;

draw((xmin, ymin) -- (xmin, ymax), L=Label("$X$", position=BeginPoint));
draw((xmin+step, ymin) -- (xmin+step, ymax), L=Label("$Y$", position=BeginPoint));

dot((xmin, x1), L=Label("$x_1$", align=W));
dot((xmin+step, y1), L=Label("$y_1$", align=E));

path p = (xmin, x1) -- (xmin+step, y1);
draw(p);
pathlabel("$(x_1, y_1)$", p, position=0.5, align=Relative(W), sloped=true);

dot((xmin, x2), L=Label("$x_2$", align=W));
dot((xmin+step, y2), L=Label("$y_2$", align=E));

path p = (xmin, x2) -- (xmin+step, y2);
draw(p);
pathlabel("$(x_2, y_2)$", p, position=0.5, align=Relative(W), sloped=true);
