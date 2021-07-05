describe("start Quran SRS V2 project", () => {
    it('Open Home page', () => {
        cy.visit("/")
        cy.title().should("contain", "Manage Students")

    });

    it('Add Student1', () => {
        // Need to visit the page explicitly otherwise csrf cookie is cleared
        cy.visit("/")
        cy.get("input#add-student").type("Student1")
        cy.get("form").submit()

        cy.get("table tbody tr td").contains("Student1")

    });

    it('Add Student2 and check whether 2 students are there', () => {
        cy.visit("/")
        cy.get("input#add-student").type("Student2")
        cy.get("form").submit()

        cy.get("table tbody tr td").contains("Student1")
        cy.get("table tbody tr td").contains("Student2")
    });
})