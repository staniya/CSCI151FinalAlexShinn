use texture_synthesis as ts;

fn main() -> Result<(), ts::Error> {
    // create a new session
    let texsynth = ts::Session::builder()
        // load multiple example image
        .add_examples(&[
            &"imgs/hiphoptest/9.jpg",
            &"imgs/hiphoptest/10.jpg",
            &"imgs/hiphoptest/11.jpg",
            &"imgs/hiphoptest/12.jpg",
        ])
        // we can ensure all of them come with same size
        // that is however optional, the generator doesnt care whether all images are same sizes
        // however, if you have guides or other additional maps, those have to be same size(s) as corresponding example(s)
        .resize_input(ts::Dims {
            width: 300,
            height: 300,
        })
        // randomly initialize first 10 pixels
        .random_init(10)
        .seed(211)
        .build()?;

    // generate an image
    let generated = texsynth.run(None);

    // save the image to the disk
    generated.save("out/hiphopoutput4.jpg")?;

    //save debug information to see "remixing" borders of different examples in map_id.jpg
    //different colors represent information coming from different maps
    generated.save_debug("out/")
}
