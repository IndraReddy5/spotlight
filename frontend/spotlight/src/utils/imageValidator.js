// imageValidator.js
import { helpers } from '@vuelidate/validators'


const imageTypes = ['image/jpeg', 'image/png', 'image/jpg', 'image/gif'];

export const isImage = helpers.withMessage('The cover image must be a valid image, only jpeg/jpg/png/gif formats are accepted', (file) => {
    if (!file) return true;
    return imageTypes.includes(file.type);
})