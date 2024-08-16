//
// usmap.js
//


let show_state_names = false;


let state_colors = {}
let state_centers = {}


function initialize_state_colors() {
    for (const state in state_data) {
        colorMode(HSB, 360, 100, 100);
        let c = color(random(360), 20, 100);
        state_colors[state] = c;
    }
}


function initialize_state_centers() {
    for (const state in state_data) {
        let sum_x = 0;
        let sum_y = 0;
        let count = 0;
        for (const polygon of state_data[state]) {
            for (const point of polygon) {
                sum_x += point[0];
                sum_y += point[1];
                count++;
            }
        }
        state_centers[state] = [sum_x/count, sum_y/count];
    }
}


function setup() {
    createCanvas(900, 500);
    initialize_state_colors();
    initialize_state_centers();
}


function transform_coordinates(p) {
    // map latitude/longitude to rect(0, 0, width, height)
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

    if (show_state_names) {
        fill(0);
        let position = transform_coordinates(state_centers[name]);
        textAlign(CENTER);
        text(name, position[0], position[1]);
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


function keyPressed() {
    if (key == 'n') {
        show_state_names = !show_state_names;
    }
}


