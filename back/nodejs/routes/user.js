const express = require('express');
const users = require('../controller/user');
const path = require('path');
const multer = require('multer');

const router = express.Router();

const upload = multer({
  storage: multer.diskStorage({
    destination(req, file, done){
      done(null, 'uploads/')
    },
    filename(req, file, done){
      // const ext = path.extname(file.originalname);
      const ext = path.extname(file.originalname);
      // done(null, path.basename(String(req.body.id),ext) +  ext)
      done(null, req.session.user_id + ext)
      // done(null, path.basename(req.session.user_id,ext) +  ext)
      // console.log(req)
    }
  })
});

// router.get('/confirm', (req, res) => {
//   users.enroll(req, res);
// });
router.post('/upload', upload.single('image'), (req, res) => {
    res.render('index',{
      is_user: req.session.is_logined, 
      user_name: req.session.user_name
  });
});
// router.post('/',(req, res) => {
//   console.log('def')
//   res.render('index');
// });
//////////////////////////

router.get('/', async (req, res, next) => {
  try {
    res.render('index', {is_user: req.session.is_logined, user_name: req.session.user_name});
  } catch (err) {
    console.error(err);
    next(err);
  }
});
<<<<<<< HEAD
router.post('/error', async (req, res) => {  users.signIn(req, res); });
router.post('/signIn', async (req, res) => {  users.signIn(req, res); });
router.post('/signUp', (req, res) => {  users.signUp(req, res); });
router.get('/signOut', (req, res) => {  users.signOut(req, res); });

router.route('/myaccount/:id')
  .get((req, res)=>{  users.getMyaccount(req, res); })
  .put((req, res)=> {  users.updateMyaccount(req, res);  })
=======
router.post('/error', async (req, res) => {
  users.signIn(req, res);
});
router.post('/signIn', async (req, res) => {
  users.signIn(req, res);
});
router.post('/signUp', upload.single('client_image'), (req, res) => {
  console.log(req.file);
  users.signUp(req, res);
});
router.get('/signOut', (req, res) => {
  users.signOut(req, res);
});
>>>>>>> 2d7782f9ca9d87daa9f83391a11323e5fb197442

module.exports = router;
