difference() {
    union() {
        translate([20, 20, 0])
        scale([500, 500, 1050])
        rotate([90, 0, 0])
        import("canned_food_01.stl", convexity=3);
    }
   
}