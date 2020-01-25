-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema order_application
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `order_application` ;

-- -----------------------------------------------------
-- Schema order_application
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `order_application` DEFAULT CHARACTER SET utf8 ;
USE `order_application` ;

-- -----------------------------------------------------
-- Table `order_application`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `order_application`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `created_at` DATETIME NOT NULL DEFAULT NOW(),
  `updated_at` DATETIME NOT NULL DEFAULT NOW() ON UPDATE NOW(),
  `first_name` VARCHAR(255) NOT NULL,
  `last_name` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) NOT NULL,
  `password` VARCHAR(255) NOT NULL,
  `phone` VARCHAR(15) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `order_application`.`menuitems`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `order_application`.`menuitems` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `created_at` DATETIME NOT NULL DEFAULT NOW(),
  `updated_at` DATETIME NOT NULL DEFAULT NOW() ON UPDATE NOW(),
  `name` VARCHAR(255) NOT NULL,
  `description` TEXT(512) NOT NULL,
  `price` DECIMAL NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `order_application`.`payments`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `order_application`.`payments` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `created_at` DATETIME NOT NULL DEFAULT NOW(),
  `updated_at` DATETIME NOT NULL DEFAULT NOW() ON UPDATE NOW(),
  `user_id` INT NOT NULL,
  `card_number` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_payment_users1_idx` (`user_id` ASC) VISIBLE,
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE,
  CONSTRAINT `fk_payment_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `order_application`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `order_application`.`orders`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `order_application`.`orders` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `created_at` DATETIME NOT NULL DEFAULT NOW(),
  `updated_at` DATETIME NOT NULL DEFAULT NOW() ON UPDATE NOW(),
  `subtotal` DECIMAL NOT NULL,
  `tax` DECIMAL NOT NULL,
  `total_amount` DECIMAL NOT NULL,
  `delivery_carryout` TINYINT NOT NULL,
  `scheduled_delivery_pickup_time` DATETIME NOT NULL,
  `user_id` INT NOT NULL,
  `payment_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_orders_users_idx` (`user_id` ASC) VISIBLE,
  INDEX `fk_orders_payment_methods1_idx` (`payment_id` ASC) VISIBLE,
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE,
  CONSTRAINT `fk_orders_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `order_application`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_orders_payment_methods1`
    FOREIGN KEY (`payment_id`)
    REFERENCES `order_application`.`payments` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `order_application`.`order_menuitems`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `order_application`.`order_menuitems` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `created_at` DATETIME NOT NULL DEFAULT NOW(),
  `updated_at` DATETIME NOT NULL DEFAULT NOW() ON UPDATE NOW(),
  `order_id` INT NOT NULL,
  `menitem_id` INT NOT NULL,
  `quantity` INT NOT NULL,
  PRIMARY KEY (`id`, `order_id`, `menitem_id`),
  INDEX `fk_orders_has_menu_items_menu_items1_idx` (`menitem_id` ASC) VISIBLE,
  INDEX `fk_orders_has_menu_items_orders1_idx` (`order_id` ASC) VISIBLE,
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE,
  CONSTRAINT `fk_orders_has_menu_items_orders1`
    FOREIGN KEY (`order_id`)
    REFERENCES `order_application`.`orders` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_orders_has_menu_items_menu_items1`
    FOREIGN KEY (`menitem_id`)
    REFERENCES `order_application`.`menuitems` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `order_application`.`addresses`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `order_application`.`addresses` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `address_id` INT NOT NULL,
  `created_at` DATETIME NOT NULL DEFAULT NOW(),
  `updated_at` DATETIME NOT NULL DEFAULT NOW() ON UPDATE NOW(),
  `street` VARCHAR(255) NOT NULL,
  `street2` VARCHAR(256) NULL,
  `city` VARCHAR(255) NOT NULL,
  `state` VARCHAR(255) NOT NULL,
  `zip_code` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`, `address_id`),
  INDEX `fk_addresses_users1_idx` (`id` ASC) VISIBLE,
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE,
  CONSTRAINT `fk_addresses_users1`
    FOREIGN KEY (`id`)
    REFERENCES `order_application`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
