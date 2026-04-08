-- ============================================================
-- Script SQL MySQL — A executer dans phpMyAdmin (onglet SQL)
-- ============================================================

-- 1. Creer la base de donnees
CREATE DATABASE IF NOT EXISTS api_people
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

-- 2. Selectionner la base
USE api_people;

-- 3. Creer la table person
CREATE TABLE IF NOT EXISTS person (
    id        INT AUTO_INCREMENT PRIMARY KEY,
    lname     VARCHAR(100) NOT NULL,
    fname     VARCHAR(100) NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- 4. Inserer les donnees initiales
INSERT INTO person (lname, fname) VALUES
    ('Diallo', 'Ali'),
    ('Sow',    'Awa'),
    ('Fall',   'Moussa');

-- 5. Verification
SELECT * FROM person ORDER BY lname;
