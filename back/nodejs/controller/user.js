const User = require('../models/user');
const fs = require('fs').promises;
const bcrypt = require('bcrypt');

let enroll = async function (req, res) {
    let id = req.session.id
    let pwd = req.session.pwd
    let email = req.session.email
    let name = req.session.name
    try{
        let image = await fs.readFile(`../uploads/${id}.jpg`, 'utf8', function(err, data){
            console.log("gkgkgkgkgk" + data);
        });
        
        // await User.create({
        //     id: id,
        //     pwd: pwd,
        //     name: name,
        //     email: email,
        //     image: image
        // }).then(()=>{
        //     res.render('index',{ signUp_succ: true });
        // }).catch(err => {
        //     res.render('index',{ duplication: true });
        // });

    }catch{
        console.log('err')
    }
}
let signUp = async function (req, res) {
<<<<<<< HEAD
    try {
        var b = await bcrypt.hash(req.body.client_password, 12);
        console.log(b);
        await User.create({
            id: req.body.client_id,
            pwd: await bcrypt.hash(req.body.client_password, 12),
            name: req.body.client_name,
            email: req.body.client_email,
            // image: req.body.client_image
        }).then(()=>{
            res.render('index',{ signUp_succ: true });
        }).catch(err => {
            console.log(err);
            res.render('index',{ duplication: true });
        });
    }
    catch { }
=======
    await User.create({
        id: req.body.client_id,
        pwd: req.body.client_password,
        name: req.body.client_name,
        email: req.body.client_email,
        image: req.body.client_image
    }).then(()=>{
        res.render('index',{ signUp_succ: true });
    }).catch(err => {
        res.render('index',{ duplication: true });
    });
>>>>>>> 2d7782f9ca9d87daa9f83391a11323e5fb197442
}
let signIn = async function (req, res) {
    try{
        const user = await User.findAll({ where:{  id: req.body.id  } });
        if (user){
            const result = await bcrypt.compare(req.body.pwd, user[0].dataValues.pwd);
            if (result){
                console.log(`${req.body.id} 님 로그인`);
    
                req.session.is_logined = true;
                req.session.user_id = req.body.id;
                req.session.user_name = user[0].dataValues.name;
                req.session.user_pwd = user[0].dataValues.pwd
                req.session.user_image = user[0].dataValues.image
                req.session.user_email = user[0].dataValues.email
                req.session.save(err => {
                    if (err) throw err;
                    res.redirect(302, '/');
                });
            }
            else {
                console.log(result);
                console.log(`로그인 실패 \n시도 => id : ${req.body.id}, pwd : ${req.body.pwd}`);
                res.render('index', { faill: true });
            }
        }

        // if ((user[0].dataValues.pwd == req.body.pwd) && (user[0].dataValues.id == req.body.id)) {
        //     console.log(`${req.body.id} 님 로그인`);
    
        //     req.session.is_logined = true;
        //     req.session.user_id = req.body.id;
        //     req.session.user_name = user[0].dataValues.name;
        //     req.session.user_pwd = user[0].dataValues.pwd
        //     req.session.user_image = user[0].dataValues.image
        //     req.session.user_email = user[0].dataValues.email
        //     req.session.save(err => {
        //         if (err) throw err;
        //         res.redirect(302, '/');
        //     });
        // }
        // else {
        //     console.log(`로그인 실패 \n시도 => id : ${req.body.id}, pwd : ${req.body.pwd}`);
        //     res.render('index', { faill: true });
        // }
    }
    catch(err){
        console.log(err);
        console.log(`로그인 실패 \n시도 => id : ${req.body.id}, pwd : ${req.body.pwd}`);
        res.render('index', { faill: true });
    }
}
let signOut = function (req, res) {
    req.session.destroy(error => {
        if (error) console.log(error)
    });
    res.redirect(302, '/');
}
let getMyaccount = function(req, res) {
    res.render('myAccount', {
        id:req.session.user_id,
        name:req.session.user_name,
        pwd:req.session.user_pwd,
        email:req.session.user_email,
      });
}

let updateMyaccount = async function (req, res) {
    try {
        const result = await User.update({  
            id: req.body.id,
            // pwd: await bcrypt.hash(req.body.pwd, 12),
            name: req.body.name,
            email: req.body.email,
        }, {
            where: { id: req.session.user_id }
        });
        req.session.user_name = req.body.name;
        req.session.user_id = req.body.id;
        req.session.user_email = req.body.user_email;
  
        if (result) res.redirect('/');
        else next('Not updated!')
      } catch (err) {
          console.error(err);
          next(err);
      }
}

module.exports = {
    signUp,
    signIn,
    signOut,
    enroll,
    getMyaccount,
    updateMyaccount
};