scale(100)
        rotate([90, 0, 0])
        import("canned_food_01.stl", convexity=3);



union() {
    cube([3, 1, 1]);
    translate([1, 1, 0])
        cube([1, 1, 1]);
}
union() {
    translate([0, 3, 0])
    cube([3, 1, 1]);
    translate([0, 4, 0])
        cube([1, 1, 1]);
}
union() {
    translate([4, 0, 0])
    cube([2, 1, 1]);
    translate([4, 1, 0])
        cube([1, 1, 1]);
}
union() {
    translate([4, 3, 0])
    cube([2, 1, 1]);
    translate([5, 4, 0])
        cube([2, 1, 1]);
}
union() {
    translate([0, 6, 0])
    cube([2, 1, 1]);
    translate([1, 7, 0])
        cube([1, 1, 1]);
    translate([1,7,1])
        cube([1,1,1]);
}

union() {
    translate([3, 6, 0])
    cube([2, 1, 1]);
    translate([3, 5, 0])
        cube([1, 1, 1]);
    translate([3, 6, 1])
        cube([1, 1, 1]);
}
union() {
    translate([7, 0, 0])
    cube([2, 1, 1]);
    translate([7, 1, 0])
        cube([1, 1, 1]);
    translate([7, 0, 1])
        cube([1, 1, 1]);
}