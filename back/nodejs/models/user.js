const Sequelize = require('sequelize');

module.exports = class User extends Sequelize.Model {
  static init(sequelize) {
    return super.init({
      id: {
        type: Sequelize.STRING(20),
        allowNull: true,
        unique: true,
        primaryKey: true
      },
      pwd: {
        type: Sequelize.STRING(100),
        allowNull: true,
      },
      name: {
        type: Sequelize.STRING(20),
        allowNull: true,
      },
      email: {
        type: Sequelize.STRING(40),
        allowNull: true,
      },
      image: {
        type: Sequelize.BLOB,
        allowNull: true,
      },
    }, {
      sequelize,
      timestamps: false,
      underscored: false,
      modelName: 'User',
      tableName: 'users',
      paranoid: false,
      charset: 'utf8',
      collate: 'utf8_general_ci',
    });
  }
  static associate (db) {
    db.User.hasMany(db.Hosting, { foreignKey: 'host_id', sourceKey: 'id' });
    db.User.hasMany(db.Participating, { foreignKey: 'user_id', sourceKey: 'id' });
  }
};
