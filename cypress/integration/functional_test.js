describe("start Quran SRS V2 project", () => {
    it('Open Home page', () => {
        cy.visit("/")
        cy.title().should("contain", "install")
    });
})