use grafos;
DELIMITER $$

CREATE PROCEDURE EliminarConexion(IN p_id_Conexion INT)
BEGIN
    DELETE FROM Conexion WHERE id_Conexion = p_id_Conexion;
END $$

DELIMITER ;

