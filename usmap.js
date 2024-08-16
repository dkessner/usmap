//
// usmap.js
//


let state_colors = {}


function initialize_state_colors() {
    for (const state in state_data) {
        colorMode(HSB, 360, 100, 100);
        let c = color(random(360), 20, 100);
        state_colors[state] = c;
    }
}


function setup() {
    createCanvas(800, 400);
    initialize_state_colors();
}


function transform_coordinates(p) {
    const x1 = -127;
    const x2 = -66;
    const y1 = 25;
    const y2 = 50;
    return [map(p[0], x1, x2, 0, width),
            map(p[1], y1, y2, height, 0)]
}


function draw_state(name) {

    polygons = state_data[name];

    for (let polygon of polygons) {
        beginShape();
        for (let point of polygon) {
            q = transform_coordinates(point); 
            vertex(q[0], q[1]);
        }
        endShape();
    }
}


function draw() {

    background(0);
    noFill();

    for (let state in state_data) {
        stroke(0);
        fill(state_colors[state]);
        draw_state(state);
    }
}


