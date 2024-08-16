//
// usmap.js
//



function setup() {
  createCanvas(800, 400);
}


function transform_coordinates(p) {
    const x1 = -120;
    const x2 = -70;
    const y1 = 30;
    const y2 = 50;
    return [map(p[0], x1, x2, 0, width),
            map(p[1], y1, y2, height, 0)]
}


function draw() {

    background(0);
    noFill();
    stroke(0, 255, 0);

    points = state_data['California'][5]
    translate(120, 30);

    beginShape();

    for (let p of points)
    {
        //console.log(p[0] + ", " + p[1]);
        q = transform_coordinates(p); 
        vertex(q[0], q[1]);
    }

    endShape();
}
