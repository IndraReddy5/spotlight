// imageValidator.js
import { helpers } from '@vuelidate/validators'


const imageTypes = ['image/jpeg', 'image/png', 'image/jpg', 'image/gif'];
const textTypes = ['text/plain']
const audioTypes = ['audio/mpeg', 'audio/mp3']

export const isImage = helpers.withMessage('The cover image must be a valid image, only jpeg/jpg/png/gif formats are accepted', (file) => {
    if (!file) return false;
    return imageTypes.includes(file.type);
})

export const isText = helpers.withMessage('only .txt format is accepted', (file) => {
    if (!file) return false;
    return textTypes.includes(file.type);
})

export const isAudio = helpers.withMessage('The audio file must be only in the format of .mp3', (file) => {
    if (!file) return false;
    return audioTypes.includes(file.type)
})