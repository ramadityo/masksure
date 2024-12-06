window.addEventListener("load", () => {
    let tl = gsap.timeline();

    tl.to("body", {
        duration: 2,
        padding: "2rem",

        ease: "expo.inOut",
    });
});
