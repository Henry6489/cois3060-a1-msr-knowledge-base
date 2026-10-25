const buttons = document.querySelectorAll(".tab-button");
const sections = document.querySelectorAll(".tab-content");

buttons.forEach((button) => {

    button.addEventListener("click", () => {

        buttons.forEach((item) => {
            item.classList.remove("active");
        });

        sections.forEach((section) => {
            section.classList.remove("active");
        });

        button.classList.add("active");

        const target = button.dataset.target;

        document
            .getElementById(target)
            .classList.add("active");

    });

});
