// Toggle open all details elements, onload
// Regardless of their initial status
// StackOverflow 43008609
const expandElements = shouldExpand => {
    let detailsElements = document.querySelectorAll("details");

    detailsElements = [...detailsElements];

    if (shouldExpand) {
        detailsElements.map(item => item.setAttribute("open", shouldExpand));
    } else {
        detailsElements.map(item => item.removeAttribute("open"));
    }
};